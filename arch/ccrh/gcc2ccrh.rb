#! ruby -Ku

if ARGV.size != 1 then
    puts "Argment Error!"
    exit
end

#Input from gcc file
begin
    gcc_asm_file = open(ARGV[0])
rescue
    puts "File Open Error!"
    exit
end


cx_asm = ""

#Convert 
while line = gcc_asm_file.gets
    line = line.gsub('.section .reset.text', "RESET .cseg text")
    
    line = line.sub('/*', ';/*')
    
    line = line.sub(/^(\s*)\*/, '\1;*')
    
    line = line.sub(/.macro\s+(\w+)/, '\1 .macro')
    
    line = line.sub(/#include\s+[<"](.+)[>"]/, '$include (\1)')
    
    line = line.sub('.global', '.extern')    
    
    line = line.gsub(/AMARG\((\w+)\)/, '\1')
    
    line = line.gsub(/FLABEL\((\w+)\)/, '\1:')
        
    line = line.gsub('~', '!')
    
    line = line.gsub('#ifdef', '$ifdef')
    
    line = line.gsub('#ifndef', '$ifndef')    
    
    line = line.gsub('#endif', '$endif')
    
    line = line.gsub('#else', '$else')    
    
    line = line.gsub('.section', '.cseg')
    
    line = line.gsub(/\.endr/i, '.endm')
    
    line = line.gsub(/\.text/i, 'text')

    line = line.gsub(/\b_fe_exception_entry\b/,'_kernel_fe_exception_entry')
    line = line.gsub(/\b_ei_exception_entry\b/,'_kernel_ei_exception_entry')
    line = line.gsub(/\b_interrupt\b/,'_kernel_interrupt')
    line = line.gsub(/\b_exit_and_dispatch\b/,'_kernel_exit_and_dispatch')
    line = line.gsub(/\b_start_dispatch\b/,'_kernel_start_dispatch')
    line = line.gsub(/\b _dispatch\b/,' _kernel_dispatch')
    line = line.gsub(/\b_dispatch\b/,'_kernel_dispatch')
    line = line.gsub(/\b_start_r\b/,'_kernel_start_r')
    line = line.gsub(/\b_stack_change_and_call_func_1\b/,'_kernel_stack_change_and_call_func_1')
    line = line.gsub(/\b_stack_change_and_call_func_2\b/,'_kernel_stack_change_and_call_func_2')
    line = line.gsub(/\b_return_main\b/,'_kernel_return_main')
    line = line.gsub(/\b_ostk\b/,'_kernel_ostk')
    line = line.gsub(/\b_ostkpt\b/,'_kernel_ostkpt')
    line = line.gsub(/\b_except_nest_cnt\b/,'_kernel_except_nest_cnt')
    line = line.gsub(/\b_nested_lock_os_int_cnt\b/,'_kernel_nested_lock_os_int_cnt')
    line = line.gsub(/\b_current_iintpri\b/,'_kernel_current_iintpri')
    line = line.gsub(/\b_pmr_setting_tbl\b/,'_kernel_pmr_setting_tbl')
    line = line.gsub(/\b_pmr_isr1_mask\b/,'_kernel_pmr_isr1_mask')
    line = line.gsub(/\b_pmr_isr2_mask\b/,'_kernel_pmr_isr2_mask')
    line = line.gsub(/\b_v850_cpu_exp_sp\b/,'_kernel_v850_cpu_exp_sp')
    line = line.gsub(/\b_v850_cpu_exp_no\b/,'_kernel_v850_cpu_exp_no')
    line = line.gsub(/\b_v850_cpu_exp_pc\b/,'_kernel_v850_cpu_exp_pc')
    line = line.gsub(/\b_call_protectionhk_main\b/,'_kernel_call_protectionhk_main')
    line = line.gsub(/\b_kerflg\b/,'_kernel_kerflg')
    line = line.gsub(/\b_isr_p_isrcb_tbl\b/,'_kernel_isr_p_isrcb_tbl')
    line = line.gsub(/\b_exit_task\b/,'_kernel_exit_task')
    line = line.gsub(/\b_p_runtsk\b/,'_kernel_p_runtsk')
    line = line.gsub(/\b_p_runisr\b/,'_kernel_p_runisr')
    line = line.gsub(/\b_default_int_handler\b/,'_kernel_default_int_handler')
    line = line.gsub(/\b_call_pretaskhook\b/,'_kernel_call_pretaskhook')
    line = line.gsub(/\b_call_posttaskhook\b/,'_kernel_call_posttaskhook')
    line = line.gsub(/\b_exit_isr2\b/,'_kernel_exit_isr2')
    line = line.gsub(/\b_callevel_stat\b/,'_kernel_callevel_stat')
    line = line.gsub(/\b_p_schedtsk\b/,'_kernel_p_schedtsk')
    line = line.gsub(/\b_isr_tbl\b/,'_kernel_isr_tbl')

    cx_asm = cx_asm  + line
end

cx_asm_file_name = File::basename(ARGV[0].sub(".S", ".asm"))
print sprintf("Output %s\n", cx_asm_file_name)

#Output to asm file
File.open(cx_asm_file_name, 'w') {|file|
 file.write cx_asm 
}
