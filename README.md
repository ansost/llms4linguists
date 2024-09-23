# Course website for `LLMs in Linguistic Research`

This website is forked from [this template](https://github.com/jonjoncardoso/quarto-template-for-university-courses). Check out their README for instructions on how to use the template. 

# 💡 How to use this template
7. Add your **course code** and **course name** to the web pages

    - If you are using VSCode, you can Ctrl + Shift + F (or ⌘ + Shift + F if you are on Mac) and replace all occurrences of `MY_COURSE_CODE` and `MY_COURSE_NAME` to the code and name of your course, respectively.
    - Or, you can manually edit those in the following files:
        - `_quarto.yml`
        - `2023/index.qmd`
        - `helpers/remove-nav.html`

8. Then move on to `_quarto.yml`. Scan through this file to spot what you want to change. What pages do you want to keep or remove from your website?

9. Next, modify the content of `index.qmd` and start working properly on your content pages under `2023/*`

10. Visualise your changes by running the Quarto website locally:

    ```bash
    quarto preview . --render all --no-browser
    ```
</details>

# 🧰 Dev Setup

On top of the setup below, I also recommend you use [VSCode](https://code.visualstudio.com/Download) as your primary IDE.

<details><summary>🐍 The Python setup</summary>

## 🕸️ Publishing the website

I recommend you set up a **GitHub Action** for this. Just follow the instructions in the official [Quarto instructions](https://quarto.org/docs/publishing/github-pages.html#publish-action).

💡 This template already comes with a GitHub workflow setup. You can find it in the [.github/workflows/publish.yml_](.github/workflows/publish.yml_) file. You just need to rename it to `.github/workflows/publish.yml` (remove the underscore at the end)

</details>