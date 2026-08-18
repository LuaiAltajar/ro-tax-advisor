import os


def init_phoenix():
    import phoenix as px
    from phoenix.otel import register

    
    register(project_name="ro-tax-advisor", auto_instrument=True)
    px.launch_app()

    return True