# Load board and initialize plot controller
board = pcbnew.LoadBoard("hellen121vag.kicad_pcb")
pc = pcbnew.PLOT_CONTROLLER(board)
po = pc.GetPlotOptions()
po.SetPlotFrameRef(False)

# Set current layer
pc.SetLayer(pcbnew.F_Cu)

# Plot single layer to file
pc.OpenPlotfile("front_copper", pcbnew.PLOT_FORMAT_GERBER, "front_copper")
print("Plotting to " + pc.GetPlotFileName())
pc.PlotLayer()
pc.ClosePlot()