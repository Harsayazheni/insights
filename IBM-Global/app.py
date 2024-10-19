from flask import Flask, render_template
import plotly
import json
from Elec_consumption import create_dashboard_plots  # Import your plotting functions

app = Flask(__name__)

@app.route('/')
def index():
    # Generate the plots
    fig1, fig2, fig3, fig4 = create_dashboard_plots()  # This function should return your Plotly figures
    
    # Convert the plots to JSON
    plot1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    plot2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    plot3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    plot4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Render the template with the plot data
    return render_template('dashboard.html', plot1JSON=plot1JSON, plot2JSON=plot2JSON, 
                           plot3JSON=plot3JSON, plot4JSON=plot4JSON)

if __name__ == '__main__':
    app.run(debug=True)