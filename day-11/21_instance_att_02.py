class Session:
	platform = "Google Meet"
	def __init__(self, topic):
		self.topic = topic

s1 = Session('Python Fundametals')
# s1.platform = "Zoom"

print(s1.platform)
print(Session.platform)
