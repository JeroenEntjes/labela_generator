    ${model_name} = providers.Factory(
        ${model_class_name}Repository,
        session=Database.session
    )
