from mako.template import Template


def file_from_template(template_file, dest, **kwargs):
    template = Template(filename=template_file)
    output = template.render(**kwargs)
    with open(dest, 'w') as f:
        f.write(output)


def append_template_to_file(template_file, dest, **kwargs):
    template = Template(filename=template_file)
    output = template.render(**kwargs)
    with open(dest, 'a') as f:
        f.write(output)
