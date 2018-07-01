from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df_data = pd.read_excel('Homework 15/dataRaw.xlsx')
df_data = df_data.T
#bb_series = "bb_"+str(df_data["index"])

@app.route("/")
def echo():
    return render_template("index.html", text="Something")

@app.route('/names')
def names():
    return render_template("names.html", namesHtml="test" )
    # """List of sample names.

    # Returns a list of sample names in the format
    # [
    #     "BB_940",
    #     "BB_941",
    #     "BB_943",
    #     "BB_944",
    #     "BB_945",
    #     "BB_946",
    #     "BB_947",
    #     ...
    # ]

    # """
@app.route("/otu")
def otu():
    return render_template("otu.html", otuHtml="test2")
    # """List of OTU descriptions.

    # Returns a list of OTU descriptions in the following format

    # [
    #     "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
    #     "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
    #     "Bacteria",
    #     "Bacteria",
    #     "Bacteria",
    #     ...
    # ]
    # """
@app.route('/metadata/<sample>')
def metadata(sample):
    return render_template("metadata.html", metadata=sample)
    # """MetaData for a given sample.

    # Args: Sample in the format: `BB_940`

    # Returns a json dictionary of sample metadata in the format

    # {
    #     AGE: 24,
    #     BBTYPE: "I",
    #     ETHNICITY: "Caucasian",
    #     GENDER: "F",
    #     LOCATION: "Beaufort/NC",
    #     SAMPLEID: 940
    # }
    # """
@app.route('/wfreq/<sample>')
def wfreq(sample):
    return render_template("wfreq.html", wfreq="test4")
    # """Weekly Washing Frequency as a number.

    # Args: Sample in the format: `BB_940`

    # Returns an integer value for the weekly washing frequency `WFREQ`
    # """
@app.route('/samples/<sample>')
def samples(sample):
    return render_template("samples.html", samples="test5")
    # """OTU IDs and Sample Values for a given sample.

    # Sort your Pandas DataFrame (OTU ID and Sample Value)
    # in Descending Order by Sample Value

    # Return a list of dictionaries containing sorted lists  for `otu_ids`
    # and `sample_values`

    # [
    #     {
    #         otu_ids: [
    #             1166,
    #             2858,
    #             481,
    #             ...
    #         ],
    #         sample_values: [
    #             163,
    #             126,
    #             113,
    #             ...
    #         ]
    #     }
    # ]
    # """
if __name__ == "__main__":
    app.run(debug=True)