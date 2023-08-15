<h1 align='center'>Symantec endpoint protection reports parser</h1>
<h2>Description</h2>
<p>The simple scripts for parse symantec endpoint protection html reports.</p>

<b>Scripts:</b>
<br>
<i><b>- sepr_parser.py</b></i> - parse html report and output txt files to folders.
<br>
<i><b>- uniq.sh</b></i> - sort and uniq all result to <b>alerts</b> folder.

<b>Folders:</b>
<br>
<li>
<b>risk_category</b> - VIRUS AND RISK DETECTION (Blocked, Quarantined, Deleted, Newly Infected, Still Infected),
strings: <b><i>"Filename: Unavailable" - exception!</i></b>
</li>
<li>
<b>av_status</b> - Protection Status Snapshot (AV Engine Off, SONAR Proactive Threat Scan Off); 
</li>

<li>
<b>alerts</b> - Uniq and sorted results; 
</li>

<hr>

<h2>Install</h2>
<pre>git clone https://github.com/J3eyond/SEPR_parser</pre>
<pre>cd SEPR_parser</pre>
<i>Create a virtual environment (optional):</i>
<pre>virtualenv venv</pre>
<i>Activate the virtual environment:</i>
<pre>source venv/bin/activate</pre>
<i>Install requirements:</i>
<pre>pip install -r requirements.txt</pre>
Give permission to launch(bash script):
<pre>chmod +x uniq.sh</pre>

<h2>Launch</h2>
<pre>python3 sepr_parser.py *<b>path to your report*</b></pre>
<br>
<pre>./uniq.sh</pre>
<h2>Requirements</h2>
<ul>
    <li>
        <b>python 3.9 +</b>
    </li>
    <li>
        <b>virtualenv==20.23.1 (optional)</b>
    </li>
</ul>