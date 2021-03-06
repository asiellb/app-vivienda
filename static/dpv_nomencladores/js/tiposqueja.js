'use strict';

function abrir_modal(url, id=null)
{
    $('#popup').load(url, function()
    {
        $(this).modal('show');
    });

    return false;
}

function cerrar_modal()
{
    $('#popup').modal('hide');
    return false;
}

var DPVTipoQuejaNom =  function () {
    let tipoqueja_form;
    let validator_form;

    const _initTipoQuejaPane = function (translations) {
        $('#tqueja-table').DataTable({
            responsive: true,
            order: [ 0, 'desc' ],
            lengthMenu: [20, 35, 50, "All"],
            sScrollX: "100%",
            language: {
                "decimal": "",
                "emptyTable": translations.emptyTable,
                "info": translations.info_init + " _START_ a _END_ de _TOTAL_ " + translations.info_end,
                "infoEmpty": translations.infoEmpty,
                "infoFiltered": "(" + translations.infoFiltered_init + " _MAX_ " + translations.infoFiltered_end + ")",
                "infoPostFix": "",
                "thousands": ",",
                "lengthMenu": translations.lengthMenu_init + " _MENU_ " + translations.lengthMenu_end,
                "loadingRecords": translations.loadingRecords,
                "processing": translations.processing,
                "search":  translations.search,
                "zeroRecords": translations.zeroRecords,
                "paginate": {
                        "first": translations.first,
                        "last": translations.last,
                        "next": translations.next,
                        "previous": translations.previous,
                }
            },
        });
    };
    const _initTipoQuejaForm =  function () {


        $.validator.setDefaults({
            errorClass: 'text-danger',
            highlight: function(element) {
                $(element).addClass('is-invalid');
            },
            unhighlight: function(element) {
                $(element).removeClass('is-invalid');
            },

			ignore: ":hidden",

            errorPlacement: function(error, element) {
                if (element[0].attributes['type'].nodeValue === 'select-one' || element[0].attributes['type'].nodeValue === 'select-multiple')
                    error.insertBefore(element.parent());
                else
                    error.insertBefore(element);
            },

        });
        $.validator.addMethod("letterswithbasicpuncandspace", function(value, element) {
            return this.optional(element) || /^[a-zA-Z0-9áéíóúÁÉÚÍÓñÑ \-.,()'"\s]+$/i.test(value);
        }, "solo puede tener letras, números, y signos de puntuación básicos");
        validator_form = tipoqueja_form.validate({
			rules: {
				nombre: {
				    maxlength: 90,
				    required: true,
                    letterswithbasicpuncandspace: true,
                    remote: {
                        url: '/nomenclador/verify_tipoqueja/',
                        type: 'GET',
                        data: {
                            id: tqueja_id,
                        },
                    },
				},
				numero: {
				    maxlength: 3,
				    required: true,
                    digits: true,
                    remote: {
                        url: '/nomenclador/verify_tipoqueja/',
                        type: 'GET',
                        data: {
                            id: tqueja_id,
                        },
                    },
				},
			},
			messages: {
				nombre: {
				    maxlength: "El nombre del tipo de queja no puede tener más de 90 caracteres.",
				    required: "El nombre del tipo de queja es obligatorio.",
                    letterswithbasicpuncandspace: "El nombre del tipo de queja solo puede tener letras, números, y signos de puntuación básicos.",
                    remote: "Ya existe otro tipo de queja registrado con ese nombre.",
				},
				numero: {
				    maxlength: "El código del tipo de queja no puede tener más de 3 dígitos.",
				    required: "El código del tipo de queja es obligatorio.",
                    digits: "El nombre del tipo de queja solo puede tener números.",
                    remote: "Ya existe otro tipo de queja registrado con ese código.",
				},
			},
		});
    };

    return {
        init: function (translations) {
            _initTipoQuejaPane(translations);
        },
        initForm: function () {
            tipoqueja_form = $('#form_tipoqueja');
            _initTipoQuejaForm();
        },
    }
}();