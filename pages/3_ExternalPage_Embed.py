# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code
import requests

def embed_external_webpage(url: str, width: int = 700, height: int = 400):
    """Embeds an external webpage using an iframe tag."""
    iframe_code = f'<iframe src="{url}" width="{width}" height="{height}"></iframe>'
    st.markdown(iframe_code, unsafe_allow_html=True)

# Call the function to embed a web page
# embed_external_webpage("https://www.co2sensei.com/")

def embed_via_fetch(url: str):
    """Fetches and embeds an external webpage content using requests."""
    response = requests.get(url)
    if response.status_code == 200:
        st.write(response.text, unsafe_allow_html=True)
    else:
        st.write(f"Failed to retrieve the webpage. HTTP Error Code: {response.status_code}")

# Call the function to embed a web page
embed_via_fetch("https://www.co2sensei.com/")

