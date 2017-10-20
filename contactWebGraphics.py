import wx

class MainWindow(wx.Frame):
	"""docstring for MainWindow"""
	def __init__(self, *arg,**kw):
		super(MainWindow, self).__init__(*arg,**kw,size=(900,600))
		self.panel=wx.Panel(self)
		self.Show()
		self.width,self.height=self.panel.GetSize()

		self.makeMenuBar()

		self.terminalInput=wx.TextCtrl(self.panel,size=(self.width/3,20),pos=(0,self.height-65))
		self.terminalInput.Bind(wx.EVT_TEXT,self.OnKeyTyped)

		self.command=''
		self.terminalOutput=wx.TextCtrl(self.panel,size=(self.width/3,self.height-65),pos=(0,0),\
			style=wx.TE_READONLY|wx.ALIGN_BOTTOM,value=self.command)

		self.panel.Bind(wx.EVT_PAINT,self.OnPaint)
		self.terminalInput.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressed)

		self.CreateStatusBar()

	def makeMenuBar(self):
		fileMenu=wx.Menu()
		fileMenu.AppendSeparator()
		exitItem=fileMenu.Append(wx.ID_EXIT)

		helpMenu=wx.Menu()
		helpItem=helpMenu.Append(-1,"&Help\tCtrl-H",'Help string')

		menuBar=wx.MenuBar()
		menuBar.Append(fileMenu,'&File')
		menuBar.Append(helpMenu,'&Help')

		self.SetMenuBar(menuBar)

		self.Bind(wx.EVT_MENU,self.OnHelp,helpItem)
		self.Bind(wx.EVT_MENU,self.OnExit,exitItem)

	def OnExit(self,event):
		self.Close(True)

	def OnHelp(self,event):
		wx.MessageBox('Help')

	def OnKeyTyped(self,event):
		event.GetString()

	def OnEnterPressed(self,event):
		self.command=self.terminalInput.GetValue()
		print(self.command)

	def OnPaint(self,event):
		dc=wx.PaintDC(self.panel)
		dc.Clear()
		dc.SetPen(wx.Pen(wx.BLACK,2))
		dc.DrawRectangle(0,0,self.width/3,self.height-65)
