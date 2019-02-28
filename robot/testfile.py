import motor as m

motor = m.MotorController()
motor.initialize()


motor.forward(5)
motor.backward(2)
