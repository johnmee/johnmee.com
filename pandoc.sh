rm static/resume.docx
pandoc pages/resume.md -f markdown+smart -t docx -s -o static/resume.docx

