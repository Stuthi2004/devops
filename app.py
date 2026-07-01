from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Bioinformatics FASTA Parser</h2>

    <form action="/parse" method="post">
        <textarea name="sequence" rows="10" cols="60"
        placeholder="Paste FASTA sequence here"></textarea><br><br>

        <input type="submit" value="Parse Sequence">
    </form>
    """

@app.route("/parse", methods=["POST"])
def parse():

    fasta = request.form["sequence"]

    lines = fasta.strip().split("\n")

    header = lines[0]

    sequence = "".join(lines[1:])

    length = len(sequence)

    gc = (sequence.count("G") + sequence.count("C")) / length * 100 if length else 0

    return f"""
    <h2>Parsing Result</h2>

    <b>Header:</b> {header}<br><br>

    <b>Sequence Length:</b> {length}<br><br>

    <b>GC Content:</b> {gc:.2f}%<br><br>

    <a href="/">Back</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)