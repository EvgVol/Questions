from fpdf import FPDF

# Создаем PDF-документ
pdf = FPDF()

# Добавляем страницу
pdf.add_page()

# Устанавливаем шрифт Arial (не поддерживает кириллицу в стандартной версии FPDF)
pdf.set_font("Arial", size=12)

# Заголовок
pdf.cell(200, 10, txt="Main Areas of Information Technology", ln=True, align='C')

# Введение
pdf.ln(10)
pdf.multi_cell(0, 10, txt="""Information technologies (IT) play an important role in the modern world. From data processing to software development, 
network solutions to artificial intelligence these technologies are constantly evolving, creating new opportunities for business, science, and people's lives. 
Information technologies cover a wide range of areas, all of which aim to improve quality of life and accelerate processes in various spheres.
""")

# Основные области информационных технологий
pdf.ln(10)
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="Main Areas of Information Technology", ln=True)

pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""1. Software Development: Creating applications and operating systems for various platforms, from mobile to server solutions.
2. Artificial Intelligence and Machine Learning: These fields have become an integral part of many industries, from medicine to finance.
3. Cybersecurity: Protecting data and systems from threats and attacks is a key area given the increasing amount of data and online transactions.
4. Cloud Computing: More and more companies are moving to cloud technologies for data storage and processing, which helps save resources and improve scalability.
5. Big Data and Analytics: Collecting and analyzing large volumes of data to gain valuable insights and improve business strategies.
""")

# Современные тенденции в IT
pdf.ln(10)
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="Modern Trends in IT", ln=True)

pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt=""". Integration of artificial intelligence into everyday processes.
. The development of 5G technologies to improve communication speeds.
. Increased use of cloud computing for storage and computing.
. The application of blockchain in various industries to improve transparency and security.
. Growing attention to data privacy and security.
""")

# Заключение
pdf.ln(10)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""Information technologies are constantly evolving and being integrated into our daily lives, transforming old approaches into new opportunities. Each area of IT plays an important role in addressing current issues and shaping the future of humanity in the digital age.
""")

# Сохранение PDF
pdf.output("IT_info.pdf")
