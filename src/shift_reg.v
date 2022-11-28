module shift_reg #(
    parameter DEPTH = 1000
) (
  input wire data_i,
  input wire reset,
  input wire clk,
  output reg data_o
);

    reg [DEPTH-1:0] register;
    assign data_o = register[DEPTH-1];

    always @(posedge clk) begin
        // if reset, set counter to 0
        if (reset) begin
            register <= 0;
        end else begin
            register[0] <= data_i;
            register[DEPTH-1:1] <= register[DEPTH-2:0];
        end
    end

endmodule
