frappe.listview_settings['Journal Voucher'].onload = function (me) {

    console.log("JV list ran");

    me.appframe.add_primary_action(__("Print Cheque/DD Deposit Slip"), function () {
        var selected = me.get_checked_items() || [];

        if (!selected.length) {
            msgprint(__("Please select Journal Vouchers."));
            return;
        }

        console.log(selected);

        // Select only submitted jv's
        for (var i in selected) {
            var d = selected[i];
            if (d.docstatus != 1) {
                msgprint(__("Journal Voucher's must be Submitted. " + d.name + " is not submitted"));
                return
            }
            if (d.voucher_type != 'Bank Voucher') {
                msgprint(__("Journal Voucher's must be of type 'Bank Voucher'."));
            }
        }

        frappe.model.with_doctype("Payin Slip", function () {
            var payin_slip = frappe.model.get_new_doc("Payin Slip");

            $.each(selected, function (i, d) {
                var detail = frappe.model.get_new_doc("Payin Slip Detail", payin_slip, "payin_slip_details");
                $.extend(detail, {
                    "jv": d.name
                });
            });

            var save_opts = {
                method: "frappe.widgets.form.save.savedocs",
                args: { doc: payin_slip, action: 'Save' }
            };


            frappe.call({
                freeze: true,
                method: save_opts.method,
                args: save_opts.args,
                callback: function (r) {
                    var w = window.open("/print?"
                        + "doctype=" + encodeURIComponent('Payin Slip')
                        + "&name=" + encodeURIComponent(r.docs[0].name)
                        + "&format=" + encodeURIComponent('Payin Slip')
                        + "&no_letterhead=1");
                    if (!w) {
                        msgprint(__("Please enable pop-ups"));
                        return;
                    }
                }
            });


        });


    }, "icon-print");
};
