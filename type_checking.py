def check_individual_type(variable: any, variable_name: str, expected_type_or_types: type | tuple[type]) -> None:
    """
        Check the type of a given variable against the expected type or types.

        Parameters:
        - variable (any): The variable to be checked.
        - variable_name (str): The name of the variable (for error messaging purposes).
        - expected_type_or_types (type or tuple of types): The expected type or a tuple of expected types for the
        variable.

        Raises:
        - TypeError: If the variable type does not match the expected type or types.
        """
    if not isinstance(variable_name, str):
        raise TypeError(f"Expected type str for variable_name. Instead got {type(variable_name)}.")
    if isinstance(expected_type_or_types, type):
        pass
    elif isinstance(expected_type_or_types, tuple):
        for item in expected_type_or_types:
            check_individual_type(item, "expected_type_or_types_item", type)
    else:
        raise TypeError(
            f"Expected type str or tuple for expected_type_or_types. Instead got {type(expected_type_or_types)}."
        )
    if not isinstance(variable, expected_type_or_types):
        raise TypeError(f"Expected type {expected_type_or_types} for {variable_name}. Instead got {type(variable)}.")


def check_type(
        variable: any = None,
        variable_name: str = None,
        expected_type_or_types: type | tuple[type] = None,
        list_of_type_checks: list[tuple[any, str, type | tuple[type]]] = None
) -> None:
    """
        Check the type of a variable against the expected type or types, or perform multiple checks in a list.

        Parameters:
        - variable (any): The variable to be checked.
        - variable_name (str): The name of the variable (for error messaging purposes).
        - expected_type_or_types (type or tuple of types): The expected type or a tuple of expected types for the variable.
        - list_of_type_checks (list of tuples): A list of tuples containing variables, their names, and their expected types.

        Raises:
        - ValueError: If improper inputs are provided.
        - TypeError: If the variable type does not match the expected type or types.
        """

    if list_of_type_checks:
        for var, var_name, expected in list_of_type_checks:
            check_individual_type(var, var_name, expected)
    elif variable is not None and variable_name is not None and expected_type_or_types is not None:
        check_individual_type(variable, variable_name, expected_type_or_types)
    else:
        raise ValueError(
            "Invalid input to check_type. Provide either a variable, variable_name, and expected_type_or_types "
            "OR a list_of_type_checks."
        )