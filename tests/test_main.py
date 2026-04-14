from unittest.mock import patch, MagicMock
from price_tracker.openai_client import (openai_caller, price_extractor)


@patch("price_tracker.openai_client.OpenAI")
def test_openai_caller(mock_openai):
    mock_client = MagicMock()
    mock_openai.return_value = mock_client

    mock_response = MagicMock()
    mock_response.output_text = "Orange who?"

    mock_client.responses.create.return_value = mock_response

    result = openai_caller()

    assert result == "Orange who?"
    mock_client.responses.create.assert_called_once()


@patch("price_tracker.openai_client.OpenAI")
def test_price_extractor(mock_openai):
    mock_client = MagicMock()
    mock_client.responses.create.return_value.output_text = "15 000 €"
    mock_openai.return_value = mock_client

    result = price_extractor("<html>Tung Tung Tung Sahur T-Shirt 15 000 €</html>", "gpt-4o-mini")

    assert "15 000 €" in result