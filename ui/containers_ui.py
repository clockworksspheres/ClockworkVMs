/********************************************************************************
** Form generated from reading UI file 'containers.ui'
**
** Created by: Qt User Interface Compiler version 5.12.9
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CONTAINERS_H
#define UI_CONTAINERS_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_containers_ui
{
public:
    QWidget *layoutWidget;
    QGridLayout *gridLayout;
    QLabel *label_panel;
    QLabel *label_baseOS;
    QComboBox *comboBox_baseOS;
    QLabel *label_windowManager;
    QComboBox *comboBox_windowManager;
    QLabel *label_4;
    QComboBox *comboBox_containerLlayers;
    QPushButton *pushButton_addLayer;
    QPushButton *pushButton_deleteLayer;
    QLineEdit *lineEdit_2;
    QLabel *label_toRun;
    QComboBox *toRun;
    QLabel *label_empty;
    QLabel *label_containerLayers;
    QLineEdit *lineEdit;
    QDialogButtonBox *buttonBox;

    void setupUi(QWidget *containers_ui)
    {
        if (containers_ui->objectName().isEmpty())
            containers_ui->setObjectName(QString::fromUtf8("containers_ui"));
        containers_ui->resize(572, 366);
        layoutWidget = new QWidget(containers_ui);
        layoutWidget->setObjectName(QString::fromUtf8("layoutWidget"));
        layoutWidget->setGeometry(QRect(30, 20, 511, 330));
        gridLayout = new QGridLayout(layoutWidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        label_panel = new QLabel(layoutWidget);
        label_panel->setObjectName(QString::fromUtf8("label_panel"));
        QFont font;
        font.setPointSize(16);
        label_panel->setFont(font);

        gridLayout->addWidget(label_panel, 0, 0, 1, 2);

        label_baseOS = new QLabel(layoutWidget);
        label_baseOS->setObjectName(QString::fromUtf8("label_baseOS"));
        label_baseOS->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout->addWidget(label_baseOS, 1, 0, 1, 2);

        comboBox_baseOS = new QComboBox(layoutWidget);
        comboBox_baseOS->setObjectName(QString::fromUtf8("comboBox_baseOS"));

        gridLayout->addWidget(comboBox_baseOS, 1, 2, 1, 1);

        label_windowManager = new QLabel(layoutWidget);
        label_windowManager->setObjectName(QString::fromUtf8("label_windowManager"));
        label_windowManager->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout->addWidget(label_windowManager, 2, 0, 1, 2);

        comboBox_windowManager = new QComboBox(layoutWidget);
        comboBox_windowManager->setObjectName(QString::fromUtf8("comboBox_windowManager"));

        gridLayout->addWidget(comboBox_windowManager, 2, 2, 1, 1);

        label_4 = new QLabel(layoutWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout->addWidget(label_4, 3, 0, 1, 1);

        comboBox_containerLlayers = new QComboBox(layoutWidget);
        comboBox_containerLlayers->setObjectName(QString::fromUtf8("comboBox_containerLlayers"));

        gridLayout->addWidget(comboBox_containerLlayers, 3, 1, 1, 2);

        pushButton_addLayer = new QPushButton(layoutWidget);
        pushButton_addLayer->setObjectName(QString::fromUtf8("pushButton_addLayer"));

        gridLayout->addWidget(pushButton_addLayer, 3, 3, 1, 2);

        pushButton_deleteLayer = new QPushButton(layoutWidget);
        pushButton_deleteLayer->setObjectName(QString::fromUtf8("pushButton_deleteLayer"));

        gridLayout->addWidget(pushButton_deleteLayer, 3, 5, 1, 1);

        lineEdit_2 = new QLineEdit(layoutWidget);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));

        gridLayout->addWidget(lineEdit_2, 4, 0, 1, 6);

        label_toRun = new QLabel(layoutWidget);
        label_toRun->setObjectName(QString::fromUtf8("label_toRun"));
        label_toRun->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout->addWidget(label_toRun, 5, 0, 1, 2);

        toRun = new QComboBox(layoutWidget);
        toRun->setObjectName(QString::fromUtf8("toRun"));

        gridLayout->addWidget(toRun, 5, 2, 1, 1);

        label_empty = new QLabel(layoutWidget);
        label_empty->setObjectName(QString::fromUtf8("label_empty"));

        gridLayout->addWidget(label_empty, 6, 0, 1, 3);

        label_containerLayers = new QLabel(layoutWidget);
        label_containerLayers->setObjectName(QString::fromUtf8("label_containerLayers"));

        gridLayout->addWidget(label_containerLayers, 7, 0, 1, 4);

        lineEdit = new QLineEdit(layoutWidget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        gridLayout->addWidget(lineEdit, 8, 0, 1, 6);

        buttonBox = new QDialogButtonBox(layoutWidget);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        gridLayout->addWidget(buttonBox, 9, 4, 1, 2);


        retranslateUi(containers_ui);

        QMetaObject::connectSlotsByName(containers_ui);
    } // setupUi

    void retranslateUi(QWidget *containers_ui)
    {
        containers_ui->setWindowTitle(QApplication::translate("containers_ui", "Construct a conatiner", nullptr));
        label_panel->setText(QApplication::translate("containers_ui", "Construct a Container", nullptr));
        label_baseOS->setText(QApplication::translate("containers_ui", "Base OS :", nullptr));
        label_windowManager->setText(QApplication::translate("containers_ui", "Window Manager :", nullptr));
        label_4->setText(QApplication::translate("containers_ui", "container layer :", nullptr));
        pushButton_addLayer->setText(QApplication::translate("containers_ui", "add ", nullptr));
        pushButton_deleteLayer->setText(QApplication::translate("containers_ui", "delete", nullptr));
        label_toRun->setText(QApplication::translate("containers_ui", "App / Service / program to run :", nullptr));
        label_empty->setText(QApplication::translate("containers_ui", "TextLabel", nullptr));
        label_containerLayers->setText(QApplication::translate("containers_ui", "Modify Command for ContainerTo Execute (if needed) :", nullptr));
    } // retranslateUi

};

namespace Ui {
    class containers_ui: public Ui_containers_ui {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CONTAINERS_H
