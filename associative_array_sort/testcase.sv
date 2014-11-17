// Example for sorting an associative array
//
// http://www.go2uvm.org/2014/11/sorting-associative-array-by-contents-in-systemverilog/

module testcase;

    int int_aa [int];
    int int_val_q [$];
    int int_index_q [$];
    int sorted_int_aa [int];
    int iter;

    localparam NUM_ENTRIES = `NUM_ENTRIES;

    initial begin: test

        $display("Started at:");
        $system("date +'%s.%N'");

        // populate array
        for (int i=0; i<NUM_ENTRIES; i++)
            int_aa[$urandom()] = $urandom();

        int_val_q = int_aa.find with (item >= 0);
        int_index_q = int_aa.find_index with (item >= 0);

        int_val_q.sort();

        foreach (int_index_q[idx]) begin: fe_1
            sorted_int_aa[int_index_q[idx]] = int_val_q[iter];
            iter++;
        end: fe_1

        $display("Finished at:");
        $system("date +'%s.%N'");

     end: test
endmodule: testcase

