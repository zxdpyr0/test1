import streamlit as st
from datetime import datetime
import json

st.set_page_config(page_title="AWR URL Opener", layout="centered")

st.title("🔗 Open Advanced Web Ranking URL")

with st.form("url_form"):
    project_id = st.text_input("Project ID")
    keyword_id = st.text_input("Keyword ID")
    search_engine_id = st.text_input("Search Engine ID")
    date_value = st.date_input("Date").strftime("%Y-%m-%d")

    submitted = st.form_submit_button("Open URLs")

    if submitted:
        now = datetime.now()
        last_save = now.strftime("%Y-%m-%d %H:%M:%S").replace(" ", "%20")

        date_range = {
            "currentDate": date_value,
            "previousDate": date_value,
            "dateRange": 5,
            "lastSave": last_save,
            "timezone": -480
        }
        date_range_str = json.dumps(date_range)

        # URLs to open
        keywords_url = f"https://app.advancedwebranking.com/ranking/keywords?project_id={project_id}"
        serp_url = (
            f"https://app.advancedwebranking.com/ranking/html?"
            f"projectId={project_id}&"
            f"keyword={keyword_id}&"
            f"searchEngine={search_engine_id}&"
            f"dateRange={date_range_str}&"
            f"serpFeature=organic&"
            f"serpFeatureAchieved=1"
        )

        # JavaScript to auto-open both URLs in new tabs
        js = f"""
        <script>
        window.open("{keywords_url}", "_blank");
        setTimeout(function() {{
            window.open("{serp_url}", "_blank");
        }}, 1500);
        </script>
        """
        st.components.v1.html(js)

        st.success("Links generated and opened in new tabs (if not blocked by browser).")
        st.markdown(f"[🔗 Keywords Page]({keywords_url})", unsafe_allow_html=True)
        st.markdown(f"[📷 SERP Screenshot]({serp_url})", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "[📄 ID Reference Sheet](https://docs.google.com/spreadsheets/d/17nJ_QQmwrMEIgivku38MrCdYpABedYndZai27AuqENY/edit?gid=2002093151#gid=2002093151)",
    unsafe_allow_html=True,
)
