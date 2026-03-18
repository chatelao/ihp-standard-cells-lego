# Build Quality Assessment

This report evaluates the stability of the 3 base layers (Substrate Low, Substrate High, and Active) for each library cell.

## Stability Metrics
- **Avg Size**: Average studs per plate in that layer (higher is better).
- **Interlocking**: A 'Yes' indicates that Layer 1 (Substrate Low) and Layer 2 (Substrate High) use perpendicular plate orientations to increase structural integrity.
- **Overall Score**: Weighted average of sizes, with a bonus for interlocking.

| Cell Name | L1 Avg Size | L2 Avg Size | L3 Avg Size | Interlocking | Stability Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| sg13g2_a21o_1 | 60.0 | 45.0 | 12.9 | No | 39.3 |
| sg13g2_a21o_2 | 42.0 | 35.0 | 12.4 | Yes | 35.7 |
| sg13g2_a21oi_1 | 22.5 | 19.3 | 6.1 | No | 16.0 |
| sg13g2_a21oi_2 | 42.0 | 35.0 | 12.4 | Yes | 35.7 |
| sg13g2_a221oi_1 | 42.0 | 35.0 | 12.4 | Yes | 35.7 |
| sg13g2_a22oi_1 | 27.5 | 23.6 | 7.5 | No | 19.5 |
| sg13g2_and2_1 | 22.5 | 19.3 | 6.1 | No | 16.0 |
| sg13g2_and2_2 | 27.5 | 23.6 | 7.5 | No | 19.5 |
| sg13g2_and3_1 | 60.0 | 45.0 | 12.9 | No | 39.3 |
| sg13g2_and3_2 | 60.0 | 45.0 | 12.9 | No | 39.3 |
| sg13g2_and4_1 | 42.0 | 35.0 | 12.4 | Yes | 35.7 |
| sg13g2_and4_2 | 60.0 | 60.0 | 10.9 | No | 43.6 |
| sg13g2_antennanp | 15.0 | 12.5 | 4.4 | No | 10.6 |
| sg13g2_buf_1 | 26.2 | 17.5 | 4.8 | No | 16.2 |
| sg13g2_buf_16 | 66.0 | 60.0 | 15.7 | No | 47.2 |
| sg13g2_buf_2 | 22.5 | 19.3 | 6.1 | No | 16.0 |
| sg13g2_buf_4 | 42.0 | 35.0 | 12.4 | Yes | 35.7 |
| sg13g2_buf_8 | 49.3 | 38.3 | 10.8 | No | 32.8 |
| sg13g2_decap_4 | 26.2 | 17.5 | 4.8 | No | 16.2 |
| sg13g2_decap_8 | 60.0 | 45.0 | 12.9 | No | 39.3 |
| sg13g2_dfrbp_1 | 60.0 | 60.0 | 15.6 | No | 45.2 |
| sg13g2_dfrbp_2 | 53.0 | 49.7 | 14.5 | No | 39.0 |
| sg13g2_dfrbpq_1 | 72.0 | 72.0 | 16.4 | No | 53.5 |
| sg13g2_dfrbpq_2 | 62.5 | 57.7 | 16.7 | No | 45.6 |
| sg13g2_dlhq_1 | 50.0 | 50.0 | 14.1 | No | 38.0 |
| sg13g2_dlhr_1 | 68.6 | 68.6 | 14.1 | No | 50.4 |
| sg13g2_dlhrq_1 | 40.5 | 40.5 | 12.7 | No | 31.2 |
| sg13g2_dllr_1 | 56.7 | 56.7 | 15.9 | No | 43.1 |
| sg13g2_dllrq_1 | 60.0 | 52.5 | 13.1 | No | 41.9 |
| sg13g2_dlygate4sd1_1 | 42.0 | 35.0 | 12.4 | Yes | 35.7 |
| sg13g2_dlygate4sd2_1 | 42.0 | 35.0 | 12.4 | Yes | 35.7 |
| sg13g2_dlygate4sd3_1 | 60.0 | 60.0 | 10.9 | No | 43.6 |
| sg13g2_ebufn_2 | 45.0 | 45.0 | 12.3 | No | 34.1 |
| sg13g2_ebufn_4 | 40.5 | 40.5 | 12.7 | No | 31.2 |
| sg13g2_ebufn_8 | 66.0 | 60.0 | 15.7 | No | 47.2 |
| sg13g2_einvn_2 | 60.0 | 60.0 | 10.9 | No | 43.6 |
| sg13g2_einvn_4 | 49.3 | 38.3 | 10.8 | No | 32.8 |
| sg13g2_einvn_8 | 53.2 | 48.8 | 13.9 | No | 38.6 |
| sg13g2_fill_1 | 15.0 | 10.0 | 3.0 | No | 9.3 |
| sg13g2_fill_2 | 20.0 | 20.0 | 4.6 | No | 14.9 |
| sg13g2_fill_4 | 26.2 | 17.5 | 4.8 | No | 16.2 |
| sg13g2_fill_8 | 42.0 | 35.0 | 12.4 | Yes | 35.7 |
| sg13g2_inv_1 | 15.0 | 12.5 | 4.4 | No | 10.6 |
| sg13g2_inv_16 | 56.7 | 56.7 | 15.9 | No | 43.1 |
| sg13g2_inv_2 | 26.2 | 17.5 | 4.8 | No | 16.2 |
| sg13g2_inv_4 | 27.5 | 23.6 | 7.5 | No | 19.5 |
| sg13g2_inv_8 | 45.0 | 45.0 | 12.3 | No | 34.1 |
| sg13g2_lgcp_1 | 40.5 | 40.5 | 12.7 | No | 31.2 |
| sg13g2_mux2_1 | 45.0 | 45.0 | 12.3 | No | 34.1 |
| sg13g2_mux2_2 | 50.0 | 50.0 | 12.5 | No | 37.5 |
| sg13g2_mux4_1 | 50.5 | 46.2 | 13.9 | No | 36.9 |
| sg13g2_nand2_1 | 26.2 | 17.5 | 4.8 | No | 16.2 |
| sg13g2_nand2_2 | 27.5 | 23.6 | 7.5 | No | 19.5 |
| sg13g2_nand2b_1 | 22.5 | 19.3 | 6.1 | No | 16.0 |
| sg13g2_nand2b_2 | 32.1 | 28.1 | 10.2 | Yes | 28.2 |
| sg13g2_nand3_1 | 22.5 | 19.3 | 6.1 | No | 16.0 |
| sg13g2_nand3b_1 | 60.0 | 45.0 | 12.9 | No | 39.3 |
| sg13g2_nand4_1 | 27.5 | 23.6 | 7.5 | No | 19.5 |
| sg13g2_nor2_1 | 26.2 | 17.5 | 4.8 | No | 16.2 |
| sg13g2_nor2_2 | 27.5 | 23.6 | 7.5 | No | 19.5 |
| sg13g2_nor2b_1 | 22.5 | 19.3 | 6.1 | No | 16.0 |
| sg13g2_nor2b_2 | 60.0 | 45.0 | 12.9 | No | 39.3 |
| sg13g2_nor3_1 | 22.5 | 19.3 | 6.1 | No | 16.0 |
| sg13g2_nor3_2 | 60.0 | 60.0 | 10.9 | No | 43.6 |
| sg13g2_nor4_1 | 27.5 | 23.6 | 7.5 | No | 19.5 |
| sg13g2_nor4_2 | 39.4 | 35.0 | 10.5 | No | 28.3 |
| sg13g2_o21ai_1 | 22.5 | 19.3 | 6.1 | No | 16.0 |
| sg13g2_or2_1 | 22.5 | 19.3 | 6.1 | No | 16.0 |
| sg13g2_or2_2 | 27.5 | 23.6 | 7.5 | No | 19.5 |
| sg13g2_or3_1 | 60.0 | 45.0 | 12.9 | No | 39.3 |
| sg13g2_or3_2 | 42.0 | 35.0 | 12.4 | Yes | 35.7 |
| sg13g2_or4_1 | 42.0 | 35.0 | 12.4 | Yes | 35.7 |
| sg13g2_or4_2 | 60.0 | 60.0 | 10.9 | No | 43.6 |
| sg13g2_sdfbbp_1 | 62.0 | 58.1 | 16.9 | No | 45.7 |
| sg13g2_sdfrbp_1 | 63.8 | 63.8 | 16.5 | No | 48.0 |
| sg13g2_sdfrbp_2 | 62.6 | 56.1 | 15.2 | No | 44.6 |
| sg13g2_sdfrbpq_1 | 62.0 | 58.1 | 16.9 | No | 45.7 |
| sg13g2_sdfrbpq_2 | 68.6 | 68.6 | 16.0 | No | 51.0 |
| sg13g2_sighold | 22.5 | 19.3 | 6.1 | No | 16.0 |
| sg13g2_slgcp_1 | 50.0 | 50.0 | 14.1 | No | 38.0 |
| sg13g2_tiehi | 26.2 | 17.5 | 4.8 | No | 16.2 |
| sg13g2_tielo | 26.2 | 17.5 | 4.8 | No | 16.2 |
| sg13g2_xnor2_1 | 42.0 | 35.0 | 12.4 | Yes | 35.7 |
| sg13g2_xor2_1 | 42.0 | 35.0 | 12.4 | Yes | 35.7 |
