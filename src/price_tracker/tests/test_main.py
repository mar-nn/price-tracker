from unittest.mock import patch, MagicMock
from price_tracker.openai_client import openaicaller


@patch("price_tracker.openai_client.OpenAI")
def test_openaicaller(mock_openai):
    mock_client = MagicMock()
    mock_openai.return_value = mock_client

    mock_response = MagicMock()
    mock_response.output_text = "Orange who?"

    mock_client.responses.create.return_value = mock_response

    result = openaicaller()

    assert result == "Orange who?"
    mock_client.responses.create.assert_called_once()