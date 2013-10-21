class RunningStats:
  def __init__(self):
    self.sum = 0
    self.count = 0
    self.squared_sum = 0

  def add(self, number):
    self.sum += number
    self.squared_sum += number * number
    self.count += 1

  def average(self):
    if self.count:
      return self.sum * 1.0 / self.count
    else:
      return None

  def variance(self):
    if self.count:
      avg = self.average()
      return self.squared_sum * 1.0 / self.count - avg * avg
    else:
      return None
