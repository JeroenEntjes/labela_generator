from mako.template import Template


def file_from_template(template_file, dest, **kwargs):
    template = Template(filename=template_file)
    output = template.render(**kwargs)
    print('going to write to', dest)
    with open(dest, 'w') as f:
        f.write(output)
