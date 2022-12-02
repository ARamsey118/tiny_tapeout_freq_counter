import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles
import numpy as np

# Stolen from https://github.com/TinyTapeout/tt02-verilog-demo/blob/main/src/test.py#L6
segments = [ 63, 6, 91, 79, 102, 109, 124, 7, 127, 103 ]

UNITS = "us"

def create_input_signal(desired_output, clk):
    max_freq = clk.frequency / 2
    desired_freq = max_freq * (desired_output + 0.5) / 10
    return 1 / desired_freq


@cocotb.test()
async def test_freq_counter(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 10, units=UNITS)
    cocotb.start_soon(clock.start())
    sig_period = 10
    async def input_sig():
        while True:
            dut.sig.value = 1
            await Timer(sig_period / 2, units=UNITS)
            dut.sig.value = 0
            await Timer(sig_period / 2, units=UNITS)
    await cocotb.start(input_sig())

    dut._log.info("reset")
    dut.rst.value = 1
    await ClockCycles(dut.clk, 10)
    dut.rst.value = 0
    depth = dut.aramsey118_freq_counter.DEPTH.value

    dut._log.info("check all segments")
    for i in range(10):
        sig_period = int(create_input_signal(i, clock))
        dut._log.info("check segment {}".format(i))


        #from IPython import embed
        #embed()
        await ClockCycles(dut.clk, depth + 10)
        assert int(dut.segments) == segments[i]
        assert int(dut.aramsey118_freq_counter.digit.value) == i
        dut._log.info("segment {} passed".format(i))
        #assert int(dut.segments.value) == segments[i]

