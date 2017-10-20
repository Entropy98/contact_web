import wx

class HelloFrame(wx.Frame):
	"""docstring for HelloFrame"""
	def __init__(self, *parent, **title):
		super(HelloFrame, self).__init__(*parent, **title,size=(500,500))
		self.panel=wx.Panel(self)

		st=wx.StaticText(self.panel,label='Hello World!',pos=(125,125))
		font=st.GetFont()
		font.PointSize+=10
		font=font.Bold()
		st.SetFont(font)

		self.makeMenuBar()

		self.CreateStatusBar()
		self.SetStatusText('Welcome to wxPython!')

		self.panel.Bind(wx.EVT_PAINT,self.OnPaint)

		vbox = wx.BoxSizer(wx.VERTICAL) 

		hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
		l1 = wx.StaticText(self.panel, -1, "Text Field") 

		hbox1.Add(l1, 1, wx.EXPAND|wx.ALIGN_RIGHT|wx.ALL,5) 
		self.t1 = wx.TextCtrl(self.panel) 

		hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_RIGHT|wx.ALL,5) 
		self.t1.Bind(wx.EVT_TEXT,self.OnKeyTyped) 
		vbox.Add(hbox1)

	def makeMenuBar(self):
		fileMenu=wx.Menu()
		helloItem=fileMenu.Append(-1,"&Hello...\tCtrl-H","Help string shown in status bar for this menu item")
		fileMenu.AppendSeparator()
		exitItem=fileMenu.Append(wx.ID_EXIT)

		helpMenu=wx.Menu()
		aboutItem=helpMenu.Append(wx.ID_ABOUT)

		menuBar=wx.MenuBar()
		menuBar.Append(fileMenu,'&File')
		menuBar.Append(helpMenu,'&Help')

		self.SetMenuBar(menuBar)

		self.Bind(wx.EVT_MENU,self.OnHello,helloItem)
		self.Bind(wx.EVT_MENU,self.OnExit,exitItem)
		self.Bind(wx.EVT_MENU,self.OnAbout,aboutItem)

	def OnExit(self,event):
		self.Close(True)

	def OnHello(self,event):
		wx.MessageBox('Hello again from wxPython')

	def OnAbout(self,event):
		wx.MessageBox('This is a wxPython Hello World sample','About Hello World 2',wx.OK|wx.ICON_INFORMATION)	

	def OnPaint(self, event):
		dc = wx.PaintDC(self.panel)
		dc.Clear()
		dc.SetPen(wx.Pen(wx.BLACK, 4))
		dc.DrawLine(10, 15, 90, 60)

	def OnKeyTyped(self, event): 
		event.GetString()


if(__name__=='__main__'):
	app=wx.App()
	frm=HelloFrame(None,title='Hello World 2')
	frm.Show()
	app.MainLoop()