/********************************************************************************
** Form generated from reading UI file 'VirtualMachineBuilder.ui'
**
** Created by: Qt User Interface Compiler version 5.12.9
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef VIRTUALMACHINEBUILDER_H
#define VIRTUALMACHINEBUILDER_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    QLabel *label_4;
    QLabel *packerLabel;
    QLabel *boxcutterLabel;
    QComboBox *osFamily;
    QComboBox *osVersions;
    QDialogButtonBox *buttonBox;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(325, 250);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_4 = new QLabel(centralwidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        QFont font;
        font.setPointSize(24);
        label_4->setFont(font);

        gridLayout->addWidget(label_4, 0, 0, 1, 1);

        packerLabel = new QLabel(centralwidget);
        packerLabel->setObjectName(QString::fromUtf8("packerLabel"));

        gridLayout->addWidget(packerLabel, 1, 0, 1, 1);

        boxcutterLabel = new QLabel(centralwidget);
        boxcutterLabel->setObjectName(QString::fromUtf8("boxcutterLabel"));

        gridLayout->addWidget(boxcutterLabel, 2, 0, 1, 1);

        osFamily = new QComboBox(centralwidget);
        osFamily->setObjectName(QString::fromUtf8("osFamily"));

        gridLayout->addWidget(osFamily, 3, 0, 1, 1);

        osVersions = new QComboBox(centralwidget);
        osVersions->setObjectName(QString::fromUtf8("osVersions"));

        gridLayout->addWidget(osVersions, 4, 0, 1, 1);

        buttonBox = new QDialogButtonBox(centralwidget);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setToolTipDuration(30);
        buttonBox->setStandardButtons(QDialogButtonBox::Apply|QDialogButtonBox::Close|QDialogButtonBox::Ok|QDialogButtonBox::Save);

        gridLayout->addWidget(buttonBox, 5, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 325, 22));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        label_4->setText(QApplication::translate("MainWindow", "Virtual Machine Builder", nullptr));
        packerLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        boxcutterLabel->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // VIRTUALMACHINEBUILDER_H
