from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
from pathlib import Path
import shutil
import markdown2


dir_path = Path(__file__).resolve().parent

env = Environment(
    loader=FileSystemLoader(dir_path / 'templates'),
    autoescape=select_autoescape(['html'])
)

articles = []
md = markdown2.Markdown(extras=['metadata'])
for article in [file for file in (dir_path / 'content').iterdir() if file.suffix == '.md']:
    with (dir_path / 'content' / article).open() as f:
        html = md.convert(f.read())
        html.file_name = article.stem
        articles.append(html)

home_template = env.get_template('index.html.jinja')
article_template = env.get_template('article.html.jinja')

(dir_path / 'web').mkdir(exist_ok=True)
with (dir_path / 'web' / 'index.html').open('w') as f:
    f.write(home_template.render(articles=articles))

(dir_path / 'web' / 'content').mkdir(exist_ok=True)
for article in articles:
    with ( dir_path / 'web' / 'content' / f'{article.file_name}.html' ).open('w') as f:
        f.write(article_template.render(article=article, metadata=article.metadata))

shutil.copy(
    (dir_path / 'styles' / 'styles.css'),
    (dir_path / 'web')
)
