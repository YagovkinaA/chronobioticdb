from django.contrib import admin
from .models import  Chronobiotic, Targets , Bioclass, Mechanism,Synonyms, Effect,Articles, PublicationRecord, ChatLog

@admin.register(Chronobiotic)
class Chronobioadm(admin.ModelAdmin):
    prepopulated_fields = {'linkname':('gname',)}
#admin.site.register(Chronobiotic)
# admin.site.register(Clinicaltrials)
admin.site.register(Bioclass)
admin.site.register(Mechanism)
admin.site.register(Synonyms)
admin.site.register(Targets)
admin.site.register(Effect)
admin.site.register(Articles)

@admin.register(PublicationRecord)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'item_type')
    list_filter = ('item_type',)
@admin.register(ChatLog)
class ChatLogAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'question', 'answer_short', 'card_names', 'time_seconds']
    list_filter = ['created_at']
    search_fields = ['question', 'answer']
    readonly_fields = ['question', 'answer', 'cards_used', 'card_names', 'time_seconds', 'created_at']

    def answer_short(self, obj):
        return obj.answer[:80] + '...' if len(obj.answer) > 80 else obj.answer
    answer_short.short_description = 'Answer'