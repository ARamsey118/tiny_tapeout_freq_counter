`default_nettype none
`timescale 1ns/1ps

/*
this testbench just instantiates the module and makes some convenient wires
that can be driven / tested by the cocotb test.py
*/

module tb (
    // testbench is controlled by test.py
    input clk,
    input rst,
    input sig,
    output [6:0] segments
   );

    // this part dumps the trace to a vcd file that can be viewed with GTKWave
    initial begin
        $dumpfile ("tb.vcd");
        $dumpvars (0, tb);
        #1;
    end

    // wire up the inputs and outputs
    wire [7:0] inputs = {5'b0, sig, rst, clk};
    wire [7:0] outputs;
    assign segments = outputs[6:0];

    // instantiate the DUT
    aramsey118_freq_counter #() aramsey118_freq_counter(
        .io_in  (inputs),
        .io_out (outputs)
        );

endmodule
