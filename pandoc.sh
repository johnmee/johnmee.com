rm static/resume.docx
pandoc pages/resume.md -f markdown -t docx -S -s -o static/resume.docx
