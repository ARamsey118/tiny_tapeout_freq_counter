module moving_avg #(
    parameter DEPTH = 1000
) (
  input wire data_i,
  input wire reset,
  input wire clk,
  output wire [$clog2(DEPTH)-1:0] avg_o
);

    reg [$clog2(DEPTH)-1:0] avg;
    assign avg_o = avg;
    wire shift_out;

    always @(posedge clk) begin
        // if reset, set counter to 0
        if (reset) begin
            avg <= 0;
        end else begin
            avg <= avg + data_i - shift_out;
        end
    end

    shift_reg #(.DEPTH(DEPTH)) shift_reg(
        .data_i(data_i),
        .reset(reset),
        .clk(clk),
        .data_o(shift_out)
    );

endmodule
