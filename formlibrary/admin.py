from .models import *

admin.site.register(TrainingAttendance, TrainingAttendanceAdmin)
admin.site.register(Distribution, DistributionAdmin)
admin.site.register(Beneficiary, BeneficiaryAdmin)
admin.site.register(FieldType, FieldTypeAdmin)
admin.site.register(CustomForm, CustomFormAdmin)
admin.site.register(CustomFormField, CustomFormFieldAdmin)
