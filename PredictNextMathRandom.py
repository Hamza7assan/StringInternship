import z3
import struct

def predict_next_math_random(sequence):
    if len(sequence) != 5:
        raise ValueError("Need exactly 5 Math.random() values to predict the next one.")

    # Important: V8 uses LIFO from the entropy pool
    sequence = sequence[::-1]

    solver = z3.Solver()
    init_state0, init_state1 = z3.BitVecs("init_state0 init_state1", 64)
    state0 = init_state0
    state1 = init_state1

    for observed_random in sequence:
        s1 = state0
        s0 = state1
        state0 = s0
        s1 ^= s1 << 23
        s1 ^= z3.LShR(s1, 17)
        s1 ^= s0
        s1 ^= z3.LShR(s0, 26)
        state1 = s1

        float_64 = struct.pack("d", observed_random + 1)
        u_long_long_64 = struct.unpack("<Q", float_64)[0]
        mantissa = u_long_long_64 & ((1 << 52) - 1)
        solver.add(z3.LShR(state0, 12) == mantissa)

    if solver.check() != z3.sat:
        raise RuntimeError("Could not solve for internal state.")

    model = solver.model()
    state0 = model[init_state0].as_long()
    state1 = model[init_state1].as_long()

    # Advance one step
    s1 = state0
    s0 = state1
    s1 ^= (s1 << 23) & ((1 << 64) - 1)
    s1 ^= (s1 >> 17) & ((1 << 64) - 1)
    s1 ^= s0
    s1 ^= (s0 >> 26) & ((1 << 64) - 1)
    state0 = s0
    state1 = s1

    next_value_bits = (state0 >> 12) | 0x3FF0000000000000
    float_64 = struct.pack("<Q", next_value_bits)
    next_random = struct.unpack("d", float_64)[0] - 1

    return next_random


# Test with your sequence
js_random_outputs =[
  0.9311600617849973,
  0.3551442693830502,
  0.7923158995678377,
  0.787777942408997,
  0.376372264303491,
  # 0.23137147109312428
]

predicted = predict_next_math_random(js_random_outputs)
print(f"Predicted next value: {predicted}")