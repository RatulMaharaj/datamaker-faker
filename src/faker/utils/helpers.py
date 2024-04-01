from ..core.field import Field


def model_to_fields(
    model: dict[str, str],
    seed,
):
    if model is None:
        return None
    else:
        updated_model = {}
        for k, v in model.items():
            if isinstance(v, dict):
                updated_model[k] = v

            updated_model[k] = Field(name=v, seed=seed)

        return updated_model
