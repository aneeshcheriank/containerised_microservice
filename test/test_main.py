from unittest.mock import patch
from click.testing import CliRunner
from main import cli  # Assuming your module is named main.py

@patch("main.summarizer")
def test_summarize_command(mock_summarizer):
    runner = CliRunner()
    result = runner.invoke(cli, ["summarize", "This is a test text."])
    
    # Assert CLI ran successfully
    assert result.exit_code == 0
    # Assert correct function was called
    mock_summarizer.assert_called_once_with(text="This is a test text.")
    # Assert no unexpected output
    assert result.output == ""

@patch("main.entity_extractor")
def test_ner_command(mock_entity_extractor):
    runner = CliRunner()
    result = runner.invoke(cli, ["ner", "Find entities in this text."])
    
    # Assert CLI ran successfully
    assert result.exit_code == 0
    # Assert correct function was called
    mock_entity_extractor.assert_called_once_with(text="Find entities in this text.")
    # Assert no unexpected output
    assert result.output == ""

def test_summarize_command_missing_argument():
    runner = CliRunner()
    result = runner.invoke(cli, ["summarize"])
    
    # Assert CLI fails due to missing argument
    assert result.exit_code != 0
    assert "Error: Missing argument 'TEXT'" in result.output

def test_ner_command_missing_argument():
    runner = CliRunner()
    result = runner.invoke(cli, ["ner"])
    
    # Assert CLI fails due to missing argument
    assert result.exit_code != 0
    assert "Error: Missing argument 'TEXT'" in result.output
