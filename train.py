from curio import sleep
from bricknil import attach, start
from bricknil.hub import PoweredUpHub
from bricknil.sensor import TrainMotor
from bricknil.process import Process
import logging

file_vitesse = "vitesse.txt"


@attach(TrainMotor, name="motor")
class Train(PoweredUpHub):
    async def run(self):
        start_vitesse = 0

        self.message_info("Running")

        while True:
            vitesse_f = open(file_vitesse, "r")
            if vitesse_f != "":
                vitesse = int(vitesse_f.read())
                self.message_info(vitesse)
                if vitesse != start_vitesse:
                    self.message_info("change speed")
                    start_vitesse = vitesse
                    await self.motor.set_speed(vitesse)
                await sleep(0.1)


async def system():
    train = Train("My train")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start(system)
