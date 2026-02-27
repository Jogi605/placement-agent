from nicegui import ui
from langchain_ollama import ChatOllama
from langchain_community.tools.tavily_search import TavilySearchResults
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from io import BytesIO
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

llm = ChatOllama(model="llama3", temperature=0.1)
search = TavilySearchResults(max_results=2)

def create_pdf_buffer(name, role, company, plan_content):
    """Generate beautiful PDF"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []
    
    # Title
    title = Paragraph(f"<b>🚀 {name}'s Placement Plan</b>", styles['Title'])
    elements.append(title)
    
    subtitle = Paragraph(f"<i>{role} at {company}</i>", styles['Normal'])
    elements.append(subtitle)
    elements.append(Spacer(1, 20))
    
    # Plan content
    for line in plan_content.split('\n'):
        if line.strip():
            if line.startswith('##'):
                pstyle = styles['Heading2']
            elif line.startswith('-') or line.startswith('*'):
                pstyle = styles['Bullet']
            else:
                pstyle = styles['Normal']
            elements.append(Paragraph(line.strip(), pstyle))
        elements.append(Spacer(1, 12))
    
    doc.build(elements)
    buffer.seek(0)
    return buffer

@ui.page('/')
def index():
    ui.markdown('# 🚀 Placement AI Agent').classes('text-h3 text-center mb-8')
    
    with ui.card().classes('w-full max-w-4xl mx-auto p-8'):
        with ui.grid(columns=2).classes('gap-4 w-full'):
            name_input = ui.input('👤 Name').props('outlined dense')
            role_input = ui.input('💼 Role').props('outlined dense')
            skills_input = ui.input('⭐ Skills').props('outlined dense')
            edu_input = ui.input('🎓 Education').props('outlined dense')
            exp_input = ui.input('💼 Experience').props('outlined dense')
            company_input = ui.input('🏢 Company').props('outlined dense')
        
        # Progress + Status
        progress = ui.linear_progress(0).classes('w-full mb-4')
        status = ui.label('Ready').classes('text-h6 mb-4')
        
        # Results area
        result_area = ui.column().classes('w-full gap-4 min-h-96')
        pdf_download = ui.button('📥 Download PDF', icon='download').classes('hidden')
        
        async def generate_plan():
            try:
                if not company_input.value:
                    ui.notify('Please enter company!', type='warning')
                    return
                
                progress.set_value(0.2)
                status.text = '🔍 Web research...'
                await asyncio.sleep(0.1)  # Allow UI to update
                
                # Tavily search (run in executor to avoid blocking)
                search_results = ""
                try:
                    query = f"{company_input.value} {role_input.value} interview"
                    results = await asyncio.get_event_loop().run_in_executor(
                        None, lambda: search.invoke({"query": query})
                    )
                    search_results = str(results)[:300] + "\n"
                except Exception as e:
                    print(f"Search error: {e}")
                    search_results = ""
                
                progress.set_value(0.5)
                status.text = '🤖 AI generating plan...'
                await asyncio.sleep(0.1)  # Allow UI to update
                
                # LLM generation (run in executor)
                prompt = f"""Placement plan for {name_input.value or 'Student'}
Role: {role_input.value or 'SDE'} at {company_input.value or 'Google'}
Skills: {skills_input.value or 'Python, DSA'}

Use research: {search_results}

Format with ## headers:
## 1. Company Overview
## 2. Resume Optimization  
## 3. Skills Gap Analysis
## 4. Interview Strategy
## 5. 5 Technical Questions
## 6. 3 HR Questions
## 7. Next Steps"""
                
                response = await asyncio.get_event_loop().run_in_executor(
                    None, lambda: llm.invoke(prompt)
                )
                plan_content = response.content
                
                # Display results
                progress.set_value(0.8)
                status.text = '✨ Rendering...'
                await asyncio.sleep(0.1)  # Allow UI to update
                
                result_area.clear()
                with result_area:
                    ui.markdown(plan_content).classes(
                        'pa-6 bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl'
                    )
                
                # Setup PDF download
                pdf_buffer = await asyncio.get_event_loop().run_in_executor(
                    None, lambda: create_pdf_buffer(
                        name_input.value or 'Student',
                        role_input.value or 'SDE', 
                        company_input.value or 'Google',
                        plan_content
                    )
                )
                
                filename = f"{name_input.value or 'student'}_{role_input.value or 'SDE'}_{company_input.value or 'company'}_plan.pdf"
                
                pdf_download.classes(remove='hidden')
                pdf_download.on_click(lambda: ui.download(pdf_buffer.getvalue(), filename))
                
                progress.set_value(1.0)
                status.text = '✅ Complete!'
                ui.notify('Plan ready! Download PDF below 👇', type='success')
                
            except Exception as e:
                status.text = f'❌ Error: {str(e)[:50]}'
                ui.notify(f'Error: {str(e)}', type='negative')
                print(f"DEBUG ERROR: {e}")
        
        # Generate button
        ui.button('✨ Generate My Plan', icon='rocket_launch', on_click=generate_plan).props('large block')
        
        # PDF button (initially hidden)
        pdf_download.props('large block color=positive')

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Placement Agent', port=8081, host='127.0.0.1', reload=False, show=True)