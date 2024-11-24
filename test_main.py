import os
import pytest
from assignment14.ascii_art.main import read_banner, parse_banner, generate_ascii_art

@pytest.fixture
def sample_banner_content():
    # Simulated banner content for testing
    
    return """ A
 #  
### 
# # 
# # 

 B
##  
### 
# # 
### """

@pytest.fixture
def sample_ascii_dict():
    return {
        'A': " A\n #  \n### \n# # \n# # ",
        'B': "##  \n### \n# # \n### "
    }

def test_read_banner(tmp_path):
    # Create a temporary banner file
    test_file = tmp_path / "test_banner.txt"
    test_file.write_text("Sample banner content")

    # Test read_banner function
    result = read_banner(str(test_file))
    assert result == "Sample banner content"

def test_parse_banner(sample_banner_content, sample_ascii_dict):
    # Test parse_banner function
    result = parse_banner(sample_banner_content)
    assert result == sample_ascii_dict

def test_generate_ascii_art(sample_ascii_dict):
    # Test ASCII art generation
    string_to_convert = "AB"
    expected_output = (
        " A  ##  \n"
        " #  ### \n"
        "### # # \n"
        "# # ### \n"
        "# #     "
    )
    result = generate_ascii_art(string_to_convert, sample_ascii_dict)
    assert result == expected_output

def test_generate_ascii_art_with_unknown_characters(sample_ascii_dict):
    # Test ASCII art generation with unknown characters
    string_to_convert = "A?B"
    expected_output = (
        " A       ##  \n"
        " #       ### \n"
        "###      # # \n"
        "# #      ### \n"
        "# #          "
    )
    result = generate_ascii_art(string_to_convert, sample_ascii_dict)
    assert result == expected_output
