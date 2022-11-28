import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles
import numpy as np

segments = [ 63, 6, 91, 79, 102, 109, 124, 7, 127, 103 ]

@cocotb.test()
async def test_7seg(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    sig = Clock(dut.sig, 20, units="us")
    cocotb.start_soon(sig.start())

    dut._log.info("reset")
    dut.rst.value = 1
    await ClockCycles(dut.clk, 10)
    dut.rst.value = 0

    dut._log.info("check all segments")
    for i in range(10):
        dut._log.info("check segment {}".format(i))
        await ClockCycles(dut.clk, 100)
        assert int(dut.segments) == segments[0]
        #assert int(dut.segments.value) == segments[i]
