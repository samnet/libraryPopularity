

## Library due diligence :+1:

Deployed [here](https://lolipop0.herokuapp.com/).
Drop me a msg if need help navigating this repo (it follows [this](http://exploreflask.com/en/latest/organizing.html) structure)
Feedback & suggestions very welcome

---

### Project Des

> The **goal is to assist the user in choosing among libraries** (aka. packages, modules ...)  when several options exist.

For instance, different JS libraries for drawing an interactive line chart exist and it might not be obvious – if you are unexperienced – which one you should go for.

To do so, the idea is to **aggregate and synthesize information on libraries**. For example, a developer hesitating between two libraries can input their names and get a summary of their respective level of popularity in terms of downloads, forum activity etc. This can avoid wasting time using a package that is deprecated, for instance.

The tool also suggests alternatives to the user’s input library(/ies). E.g., if the name of a deprecated library (that might have happened to have loads of followers on GitHub and an otherwise very sleek website) is entered, it suggests better libraries for doing similar tasks.

---
### Project Org

The project is **open source**. I think that having one screen is enough. The simpler, the better.

Albeit being modest in its scope, I think it can be interesting due to, besides the value it creates for the user, the **questions raised by the building of a ranking & recommendation system**. E.g., 1. How do you come up with alternatives propositions when the user enters a specific library? 2. Where do you find data on download volume for specific libraries? 3. How do you transform the data on search popularity found on Google Trend into something meaningful? Loads of issues to be tackled creatively.

I made a prototype of the platform, using R as an example (since I happen to use that language at work). If familiar with the Python/JS/C++ (or any language really) infrastructure, why not build this site together?

---

### Project Spec

**One screen** with two select inputs (a list of libraries organized by language, and a list of possible tasks) and some visualizations made with d3.js (or is there a better library?).

The **first input** is simply the list of libraries the user is initially interested in. The **second input** is a list of “task classifiers” the user wants to achieve. E.g., [“Scientific Computing”, “Simulation”]. That second input enables us to come up with alternative suggestions.

The **radar graph** summarizes how popular a (some) package(s) are, using various metrics (the axes of the radar) as of the time of the request, e.g., number of times a package has been downloaded, popularity of its associated SO tag, etc. The **time series** shows how (an aggregate measure of) the package’s popularity has evolved. The **weighted relation map** describes what package the input is most often associated with.
