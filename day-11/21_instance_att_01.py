class Session:
	def __init__(self, platform, topic):
		self.platform = platform
		self.topic = topic

s1 = Session('Google Meet', 'Python Fundametals')
s2 = Session('Zoom', 'Django')

print(s1.topic)
print(s2.platform)
