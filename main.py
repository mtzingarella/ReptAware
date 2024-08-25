#creater a datagrabber object
import datatools.datagrabber as dg

data_grabber = dg.DataGrabber()
params = ('nerodia',)
#data = data_grabber.test()

data_grabber.get_data('sp_GetTotalObservations', params)