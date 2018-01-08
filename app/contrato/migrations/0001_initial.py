# Generated by Django 2.0.1 on 2018-01-08 16:03

import django.core.validators
from django.db import migrations, models
import django_brfied.django_brfied.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipo', '0001_initial'),
        ('django_brfied', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacao', models.CharField(max_length=250, validators=[django.core.validators.RegexValidator(regex='^\\d*/\\d{4} .+')], verbose_name='Identificação')),
                ('link', models.URLField()),
                ('programa', django_brfied.django_brfied.models.ForeignKey(on_delete=None, to='tipo.Programa', verbose_name='Programa')),
            ],
            options={
                'verbose_name': 'Edital',
                'verbose_name_plural': 'Editais',
            },
        ),
        migrations.CreateModel(
            name='Prestador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco_logradouro', models.CharField(max_length=150, verbose_name='Logradouro')),
                ('endereco_numero', models.CharField(max_length=150, verbose_name='Número')),
                ('endereco_complemento', models.CharField(blank=True, max_length=150, null=True, verbose_name='Complemento')),
                ('endereco_bairro', models.CharField(max_length=150, verbose_name='Bairro')),
                ('endereco_cep', django_brfied.django_brfied.models.CEPField(mask='99999-999', mask_stored=True, max_length=9, verbose_name='CEP')),
                ('endereco_referencia', models.CharField(max_length=150, verbose_name='Referência')),
                ('endereco_zona', models.CharField(choices=[('Urbana', 'Urbana'), ('Rural', 'Rural')], max_length=150, verbose_name='Zona residencial')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('nome_civil', models.CharField(max_length=255, verbose_name='Nome civil')),
                ('nome_social', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome social')),
                ('nome_apresentacao', models.CharField(max_length=255, verbose_name='Nome')),
                ('nome_mae', models.CharField(max_length=255, verbose_name='Nome da mãe')),
                ('nome_pai', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome do pai')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('sexo', django_brfied.django_brfied.models.SexoField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('F', 'Não declarado')], max_length=1, verbose_name='Sexo')),
                ('numero_siape', models.CharField(blank=True, max_length=7, null=True, verbose_name='Número do SIAPE')),
                ('banco', models.CharField(blank=True, max_length=250, null=True, verbose_name='Banco')),
                ('agencia', models.CharField(blank=True, max_length=250, null=True, verbose_name='Agência')),
                ('conta_corrente', models.CharField(blank=True, max_length=250, null=True, verbose_name='Conta')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('endereco_municipio', django_brfied.django_brfied.models.MunicipioField(on_delete=None, to='django_brfied.Municipio', verbose_name='Município')),
            ],
            options={
                'verbose_name': 'Prestador',
                'verbose_name_plural': 'Prestadores',
            },
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_horaria', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(40)], verbose_name='Função')),
                ('edital', django_brfied.django_brfied.models.ForeignKey(on_delete=None, to='contrato.Edital', verbose_name='Edital')),
                ('funcao', django_brfied.django_brfied.models.ForeignKey(on_delete=None, to='tipo.Funcao', verbose_name='Função')),
            ],
            options={
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
        migrations.CreateModel(
            name='Vinculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eh_servidor', models.BooleanField(verbose_name='É servidor?')),
                ('data_empenho', models.DateField(blank=True, null=True, verbose_name='Data do empenho')),
                ('numero_empenho', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número do empenho')),
                ('valor_total_empenho', models.FloatField(blank=True, null=True, verbose_name='Valor total do empenho')),
                ('valor_carga_horaria', models.FloatField(verbose_name='Valor por hora')),
                ('data_inicio_previsto', models.DateField(verbose_name='Data de início previsto')),
                ('data_fim_previsto', models.DateField(verbose_name='Data de fim previsto')),
                ('data_inicio', models.DateField(blank=True, null=True, verbose_name='Data de início real')),
                ('data_fim_real', models.DateField(blank=True, null=True, verbose_name='Data de fim real')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('prestador', django_brfied.django_brfied.models.ForeignKey(on_delete=None, to='contrato.Prestador', verbose_name='Prestador')),
                ('vaga', django_brfied.django_brfied.models.ForeignKey(on_delete=None, to='contrato.Vaga', verbose_name='Vaga')),
            ],
            options={
                'verbose_name': 'Vínculo',
                'verbose_name_plural': 'Vínculos',
            },
        ),
    ]
