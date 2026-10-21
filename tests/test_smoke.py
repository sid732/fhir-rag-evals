import fhir_rag


def test_package_imports_from_install() -> None:
    # Fails if the src layout or build backend is misconfigured.
    assert fhir_rag.__name__ == "fhir_rag"
