# BI_ass3

Short description
A collection of Business Intelligence assignment 3 materials and notebooks demonstrating data analysis, visualizations and report generation for the course assignment.

Contents
- notebooks/ — primary Jupyter notebooks with analysis and visualization (open in Jupyter or GitHub).
- data/ — local sample datasets or links (if present).
- results/ — output tables, figures and exported reports.
- README.md — this file.

What I implemented
- Data ingestion and cleaning pipelines for provided datasets.
- Exploratory data analysis with summary statistics and visualizations.
- Insights and conclusions documented in the notebooks and exportable reports.
- Reproducible notebooks, with instructions so a reviewer can re-run the analysis.

How to run
1. Clone the repository:
   git clone https://github.com/milialeksic/BI_ass3.git
2. Create a Python environment (recommended):
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
3. Install dependencies:
   pip install -r requirements.txt
   (If requirements.txt is not present, install jupyter, pandas, matplotlib, seaborn, numpy)
4. Start Jupyter and open the notebooks:
   jupyter lab
   or
   jupyter notebook

Notes
- If the dataset is large or not included, add the data files under data/ or update the notebook cells that download data.
- Results and images are stored in results/ where available.

Key files to show reviewers
- notebooks (main analysis)
- results/ and any exported PDF reports

Contact
For questions about the implementation, see my GitHub profile: https://github.com/milialeksic
