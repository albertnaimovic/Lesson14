import logging
import time
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
def consume_gas_level(starting_level: int = 50, engine_runing: bool = False) -> int:
    if engine_runing:
        logging.debug(f"Consuming gas at this {starting_level} level")
        return starting_level - 5
    else:
        logging.critical("Car can't consume gas, because it's turned off!")
        raise ValueError("Engine is not running, can't consume gas!")
def car_toggle_switch(state: bool = False) -> bool:
    if state:
        logging.debug("Car was turned on.")
        print("I'm turned on ;)")
    else:
        logging.debug("Car was turned off.")
        print("Unfortunately I'm turned off :(")
    return state
def drive() -> None:
    car_state = car_toggle_switch(True)
    gas_level = 30
    logging.debug(f"Car has {gas_level}% of fuel")
    while gas_level > 0:
        message = f"WROOOOM wrom, I have this much {gas_level} in tank"
        gas_level = consume_gas_level(gas_level, car_state)
        print(message)
        time.sleep(1)
    print("I ran out of gas")
    car_state = car_toggle_switch()
drive()