import solara


@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
        ## A Solara template for Geospatial Applications
        
        ### Introduction

        **A collection of [Solara](https://github.com/widgetti/solara) web apps for geospatial applications.**

        Just a proof-of-concept for now. Not all features are working yet. More features will be added in the future. Click on the menu above to see the other pages.

        - Web App: <https://giswqs-solara-template.hf.space>
        - GitHub: <https://github.com/opengeos/solara-template>
        - Hugging Face: <https://huggingface.co/spaces/giswqs/solara-template>

        """

        solara.Markdown(markdown)
