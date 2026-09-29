"""肉类加工核心逻辑：肉品、冷库、检疫和出库。"""

import json


def new_game():
    return {"batches": {}, "cold_load": 0, "cold_capacity": 2, "meat": 100, "loss": 0, "day": 1, "batch_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    return json.loads(text)


def store(state, batch_id, amount):
    if batch_id in state["batches"]:
        return False
    state["batches"][batch_id] = amount
    state["meat"] -= amount
    return True


def receive(state, batch_id):
    if state["cold_load"] >= state["cold_capacity"]:
        return False
    state["cold_load"] += 1
    return True


def fee(state, batch_id, end_day):
    return end_day - state["day"]


def cancel(state, batch_id):
    amount = state["batches"].pop(batch_id, 0)
    state["meat"] += amount
    return True


def output(state, amount):
    if state.get("cold_fault"):
        return False
    return True


def spoil(state):
    state["loss"] += 10
    return state["loss"]


def inspect(state, batch_id):
    if not state.get("quarantine"):
        return False
    return True


def main():
    print("肉类加工 - 命令: store/receive/fee/cancel/output/spoil/inspect/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
